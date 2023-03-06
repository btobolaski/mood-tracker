{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-22.11";
    utils.url = "github:numtide/flake-utils";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    flake-compat = {
      url = "github:edolstra/flake-compat";
      flake = false;
    };
  };

  outputs = { self, nixpkgs, utils, poetry2nix, ... }:
    let out = system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
        inherit (poetry2nix.legacyPackages.${system}) mkPoetryEnv mkPoetryApplication;
        python = pkgs.python310;
        pythonEnv = mkPoetryEnv {
          inherit python;
          projectDir = ./.;
          preferWheels = true;
        };
        commonPackages = [
          pythonEnv
          pkgs.poetry
          pkgs.black
          pkgs.gnumake
          pkgs.git-crypt
        ];
        package = mkPoetryApplication {
          inherit python;
          projectDir = ./.;
          preferWheels = true;
        };
        docker = pkgs.dockerTools.buildLayeredImage {
          name = "docker.net.tobolaski.com/r/mood-tracker";
          maxLayers = 120;
          config = {
            User = "1000:1000";
            ExposedPorts = { "8000/tcp" = {}; };
            Env = [ "STATIC_ROOT=${./staticfiles}" ];
            Cmd = ["${package.dependencyEnv}/bin/python" "${./server.py}"];
          };
        };
      in
      {
        devShells ={
          default = pkgs.mkShell {
            buildInputs = commonPackages;
            shellHook = ''
              rm -f python
              ln -s ${pythonEnv} python
            '';
          };
        };
        packages = {
          application = package;
          docker = docker;
        };
        defaultPackage = docker;
      }; in with utils.lib; eachSystem defaultSystems out;
}
