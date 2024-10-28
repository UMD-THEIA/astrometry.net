{
  description = "Build environment for Astrometry.net Code";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.x86_64-linux.default = pkgs.mkShell
        {
          nativeBuildInputs = with pkgs; [
            # gcc14
            libgcc
            gdb
            valgrind
            splint
            cairo
            netpbm
            libpng
            libjpeg
            libz
            bzip2
            python311
            python311Packages.numpy
            python311Packages.astropy
            swig4
            cfitsio

          ];

          shellHook = ''
            make install INSTALL_DIR=./build/astrometry
          '';


        };
    };

}

