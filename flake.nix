{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-22.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in rec {
        packages = flake-utils.lib.flattenTree rec {
          monical = pkgs.python3Packages.buildPythonPackage rec {
            name = "monical";
            src = self;
            meta = {
              mainProgram = "monical";
            };
            propagatedBuildInputs = [
              pkgs.python3Packages.pygame
            ];
          };
        };
        defaultPackage = packages.monical;
      });
}

