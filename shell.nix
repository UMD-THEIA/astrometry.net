{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell {
  nativeBuildInputs = with pkgs.buildPackages; [
    libgcc
    gnumake
    file


    cairo
    netpbm
    libpng
    libjpeg
    libz
    bzip2
    zlib


    python311
    python311Packages.numpy
    python311Packages.astropy
    python311Packages.scipy
    python311Packages.setuptools
    python311Packages.pillow
    python311Packages.tkinter
    python311Packages.wheel
    python311Packages.matplotlib


    swig4
    cfitsio
    gsl

    pkg-config
    wcslib
  ];
  shellHook =
    ''
      make -j
      make py -j
      make extra
      make install INSTALL_DIR=./build
    '';
}
