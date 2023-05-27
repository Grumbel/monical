{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in rec {
        packages = rec {
          default = monical;

          monical = pkgs.python3Packages.buildPythonPackage rec {
            pname = "monical";
            version = "0.0.0";

            src = ./.;

            propagatedBuildInputs = with pkgs; [
              python3Packages.pygame
            ];
          };
        };

        apps = rec {
          default = monical;
          monical = flake-utils.lib.mkApp {
            drv = packages.monical;
            exePath = "/bin/monical";
          };
        };
      }
    );
}

