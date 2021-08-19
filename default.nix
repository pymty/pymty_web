{ pkgs ? (import ./nixpkgs.nix { }).pkgs }:
let
  python = pkgs.python39;
  projectDir = ./.;
  inherit(pkgs) poetry2nix;
in
with poetry2nix; {
  app = mkPoetryApplication {
    inherit python projectDir;
  };

  env = mkPoetryEnv {
    editablePackageSources = {
      pymty = ./.;
    };
    inherit python projectDir;
  };
}
