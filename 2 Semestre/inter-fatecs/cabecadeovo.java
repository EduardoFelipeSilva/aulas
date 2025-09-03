import java.util.Scanner;

public class cabecadeovo {
    public static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        long maiorSoma = Long.MIN_VALUE;

        long min = scanner.nextInt();
        long maior = scanner.nextInt();
        long resposta = maior;

        for (long i = maior; i >= min; i--) {
            long valor = i;
            long total = 0;
            while (valor != 0) {
                total += valor % 10;
                valor /= 10;
            }
            if (total >= maiorSoma) {
                maiorSoma = total;
                resposta = i;
            }
        }

        System.out.println(resposta);
    }
}
