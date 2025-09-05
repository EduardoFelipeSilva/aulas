import java.util.Scanner;
public class App {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        Turma turma = new Turma(3, "3Semestre_ADS");

        int opcao = 0;

        do{
            try {
                System.out.println("\n [1] Inserir \n [2] Buscar \n [3] Remover \n [4] Listar \n [5] Capacidade da turma \n [0] Sair");
                System.out.println("Opcao: ");
                opcao = Integer.parseInt((sc.nextLine()));

                switch(opcao){
                    case 1:
                        System.out.print("RA: ");
                        int ra = Integer.parseInt(sc.nextLine());

                        System.out.print("Nome: ");
                        String nome = sc.nextLine();

                        boolean status = turma.inserir(new Aluno(ra,nome));

                        System.out.println(status ? "Inserido com Sucesso": "Falha ao inserir");
                        break;
                    case 2:
                        System.out.print("RA: ");
                        ra = Integer.parseInt(sc.nextLine());
                        Aluno a = turma.localizarRa(ra);
                        System.out.println(a!=null ? "Nome: "+ a.getNome() : "Não encontrado");
                        break;
                    case 3:
                        System.out.print("RA: ");
                        ra = Integer.parseInt(sc.nextLine());
                        System.out.println(turma.remover(ra)? "Removido" : "Não localizado");
                        break;
                    case 4:
                        for(Aluno al: turma.listar()){
                            System.out.println(al.getRa()+"|"+al.getNome());
                        }
                        System.out.println("Vagas livres: "+turma.capacidadeTurma());
                        break;
                    case 5:
                        System.out.println("Capacide da turma"+turma.capacidadeTurma());
                        break;
                    case 0:
                        System.out.println("Encerrado");
                    default:
                        System.out.println("Opção inválida");
                        break;
                }
            } catch (Exception e) {
                // TODO: handle exception
            }

        } while (opcao != 0 );
            sc.close();
        

        Aluno al1 = new Aluno(1, "Eduardo");
        Aluno al2 = new Aluno(2, "Vinicius");
        Aluno al3 = new Aluno(3, "Davi");

        System.out.println(turma.capacidadeTurma());
        turma.inserir(al1);
        turma.inserir(al2);
        turma.inserir(al3);
        System.out.println(turma.capacidadeTurma());
    }
}
