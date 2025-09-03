public class App {
    public static void main(String[] args) throws Exception {
        
        // instaciando um objeto

        // Toda classe que tem um construtor, existe a obrigatoriedade em 
        // preecher todos os valores no ato da criação

        // CTLR espaço

    Endereco e = new Endereco(null,null,null,null,null,null,0);

    // atribundo ou modificando valores

    e.setLogradouro("Rua jão de baros");
    e.setNumero(300);

    // Recuperando e exibindo valores
    System.out.println(e.getLogradouro());
    System.out.println(e.getNumero());

    }
}
