import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class mesada {
    public static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int filhos = scanner.nextInt();
        int totalMesada = scanner.nextInt();
        int categorias = scanner.nextInt();

        int resto = totalMesada / filhos % 10;
        int totalPrimeirosFilhos = totalMesada / filhos - resto;
        int totalUltimoFilho = totalMesada / filhos + resto * filhos;
        List<Integer> valorPrimeirosFilhos = valorGasto(totalPrimeirosFilhos, categorias);
        List<Integer> valorUltimoFilho = valorGasto(totalUltimoFilho, categorias);

        for (int i = 0; i < filhos - 1; i++) {
            for (int j = 0; j < valorPrimeirosFilhos.size(); j++) {
                if (j > 0) {
                    System.out.print(" ");
                }
                System.out.print(valorPrimeirosFilhos.get(j));
            }
            System.out.println();
        }

        for (int j = 0; j < valorUltimoFilho.size(); j++) {
                if (j > 0) {
                    System.out.print(" ");
                }
                System.out.print(valorUltimoFilho.get(j));
            }
            System.out.println();
    }

    public static List<Integer> valorGasto(int total, int categorias) {
        List<Integer> list = new ArrayList<>();
        while (total >= 30 && categorias > 0) {
            list.add(30);
            total -= 30;
            categorias--;
        }
        while (total >= 20 && categorias > 0) {
            list.add(20);
            total -= 20;
            categorias--;
        }
        while (total >= 10 && categorias > 0) {
            list.add(10);
            total -= 10;
            categorias--;
        }
          while (categorias > 0) {
            list.add(0);
            categorias--;
          }
          return list;
    }
}
