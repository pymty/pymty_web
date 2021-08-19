{}:
let
  date = "2021-08-18";
  version = "unstable";
  #  git ls-remote https://github.com/NixOS/nixpkgs nixos-unstable
  rev = "253aecf69ed7595aaefabde779aa6449195bebb7";
  src = builtins.fetchTarball {
    url = "https://github.com/nixos/nixpkgs/archive/${rev}.tar.gz";
    sha256 = "14szn1k345jfm47k6vcgbxprmw1v16n7mvyhcdl7jbjmcggjh4z7";
  };
  pkgs = import "${ src }" {};
in
  { inherit src pkgs; }
