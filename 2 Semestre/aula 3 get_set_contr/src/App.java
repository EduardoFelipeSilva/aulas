public class App {
    public static void main(String[] args) throws Exception {
        // Toda vez que quer utilizar classe precisa criar um objeto

        Aluno a = new Aluno(1,"eduardo","27-04-1998","39393","3939393","eduardo");

        // é necessario mencionar o nome do objeto para utiliza
        // NomedoObjeto.variavel ou nomeObjeto.Metodo

        // Utilizando metodo Setter
        a.setNome("Eduardo Felipe");
        
        // a.nome = "Eduardo Felipe";
        a.exibirDados();

        // re -atribuir valor
        a.setNome(null);

        a.exibirDados();

        System.out.println(a.getNome());
    }
}
