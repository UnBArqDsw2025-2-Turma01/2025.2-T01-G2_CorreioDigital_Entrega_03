package com.correiodigital.builder;

public class BuilderDemo {
    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("CORREIO DIGITAL - DEMONSTRAÇÃO DO PADRÃO BUILDER");
        System.out.println("Sistema de Criação de Usuários");
        System.out.println("=".repeat(70));

        // Criar usuário básico
        Usuario novoUsuario = new Usuario.UsuarioBuilder()
            .setNome("Marquinhos")
            .setEmail("Marcãoa@example.com")
            .setSenha("senhaForte123")
            .build();

        // Criar usuário completo
        Usuario usuarioCompleto = new Usuario.UsuarioBuilder()
            .setNome("Sarinha")
            .setEmail("Sarão@example.com")
            .setSenha("outraSenha456")
            .setBio("Desenvolvedora Java e entusiasta de Design Patterns.")
            .build();

        // Mostrar resultados
        System.out.println("\nUsuário Básico:");
        System.out.println("Nome: " + novoUsuario.getNome());
        System.out.println("Email: " + novoUsuario.getEmail());

        System.out.println("\nUsuário Completo:");
        System.out.println("Nome: " + usuarioCompleto.getNome());
        System.out.println("Email: " + usuarioCompleto.getEmail());
        System.out.println("Bio: " + usuarioCompleto.getBio());
    }
}