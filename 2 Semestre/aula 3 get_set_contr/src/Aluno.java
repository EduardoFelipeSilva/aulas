import java.util.Date;

public class Aluno {
    private int ra;
    private String nome, dataNascimento, cpf, telefone, email;

    // Todo construtor e feito apos a declaração de variaveis
    // A função do construtor é definidir todas as variaveis de uma vez

    public Aluno(int ra, String nome, String dataNascimento ,String cpf, String telefone, String email){

        this.ra = ra;
        if (validaNome(nome)){
            this.nome = nome;
        }
        this.dataNascimento = dataNascimento;
        this.cpf = cpf;
        this.telefone = telefone;
        this.email = email;
    }

    public void exibirDados(){
        System.out.println("O Nome é: "+nome);
        System.out.println("O Telefone é: "+telefone);
        System.out.println("O RA é: "+ra);
        System.out.println("A Data de Nascimento é: "+dataNascimento);
        System.out.println("O cpf é: "+cpf);
        System.out.println("O email é: "+email);
    }
    // Verificar se o nome ta vazio e nao mudar ele pelo metodo set
    public void setNome(String entrada){
        if (entrada == null || entrada.trim().isEmpty()) {
            System.out.println("O nome esta vazio");
        } else {
            this.nome = entrada;
        }

        //  ou

        // if (validaNome(entrada)){
        //     this.nome = nome;
        // }
    }
        // Verificar se o nome ta vazio e nao mudar ele pelo metodo de metodo pra poder reutilizar
    public boolean validaNome(String nome) {
        if (nome == null || nome.trim().isEmpty()) {
            System.out.println("O nome esta vazio");
            return false;
        } else {
            return true;
        }
    }

    //  recuperar a informação sem passar pra print
    public String getNome(){
        return this.nome;
    }

    
}

