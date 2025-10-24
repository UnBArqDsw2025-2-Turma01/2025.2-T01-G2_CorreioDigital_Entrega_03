package com.correiodigital.builder;

public class Usuario {
    private String nome;
    private String email;
    private String senha;
    private String bio;

    private Usuario(UsuarioBuilder builder) {
        this.nome = builder.nome;
        this.email = builder.email;
        this.senha = builder.senha;
        this.bio = builder.bio;
    }

    public String getNome() { return nome; }
    public String getEmail() { return email; }
    public String getBio() { return bio; }

    public static class UsuarioBuilder {
        private String nome;
        private String email;
        private String senha;
        private String bio;

        public UsuarioBuilder setNome(String nome) {
            this.nome = nome;
            return this;
        }

        public UsuarioBuilder setEmail(String email) {
            this.email = email;
            return this;
        }

        public UsuarioBuilder setSenha(String senha) {
            this.senha = senha;
            return this;
        }

        public UsuarioBuilder setBio(String bio) {
            this.bio = bio;
            return this;
        }

        public Usuario build() {
            return new Usuario(this);
        }
    }
}