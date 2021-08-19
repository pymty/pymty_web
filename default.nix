{ pkgs ? (import ./nixpkgs.nix { }).pkgs }:
let
  python = pkgs.python39;
  projectDir = ./.;
  inherit(pkgs) poetry2nix;
  overrides = poetry2nix.overrides.withDefaults (
    self: super: {
      cheroot = super.cheroot.overridePythonAttrs (
        old: {
          buildInputs = (old.buildInputs or  []) ++ [ self.setuptools-scm-git-archive ];
        }
      );
    }
  );
in
{
  app = poetry2nix.mkPoetryApplication {
    inherit python projectDir overrides;
  };

  env = poetry2nix.mkPoetryEnv {
    editablePackageSources = {
      pymty = ./.;
    };
    inherit python projectDir overrides;
  };
}
