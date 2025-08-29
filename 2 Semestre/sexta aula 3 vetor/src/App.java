import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {

        // Criando um array de inteiro de tamanho 5
        int[] teste = new int[5];

        // Colocando os elementos do array pela posição no array
        teste[0] = 10;
        teste[1] = 20;
        teste[2] = 30;
        teste[3] = 40;
        teste[4] = 50;

        // Exibindo um elemento do array pela sua posição
        System.out.println(teste[0]);
        System.out.println(teste[1]);

        // Recuperando elementos do array pela sua posição
        int e1 = teste[0];
        int e2 = teste[1];

        System.out.println("O conteudo: "+e1);
        System.out.println("O conteudo: "+e2);

        // Percorrer o array (sequencial) com for
        for(int i = 0; i<teste.length;i++){
            System.out.println("A posição do array é"+i);
            System.out.println("O elemento"+teste[i]);
        }

        // Criando um array de tamanho implicito

        String [] teste2 = {"Edu","Vini","Davi","Kaue"};
        // Percorrendo o array(sequencialmente) com for-each

        for(String testes:teste2){
            System.out.println(testes);
        }

        // Realiazando um print no vetor
        System.out.println(Arrays.toString(teste2));

        // Quantidade de elementos que ha no vetor: Length
        System.out.println(teste2.length);

        // Clonar um vetor: Clone
        String [] copia = teste2.clone();

        // Copiando uma parte do vetor para outro: CopyOf
        String[] copia_parcial = Arrays.copyOf(teste2,2);
        System.out.println(Arrays.toString(copia_parcial));

        // Ordenando valores dentro do array
        Arrays.sort(teste2);
        System.out.println(Arrays.ToString(teste2));
    }
    
}
