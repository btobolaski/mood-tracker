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
        inherit (poetry2nix.legacyPackages.${system}) mkPoetryEnv;
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
        ];
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
      }; in with utils.lib; eachSystem defaultSystems out;
}
