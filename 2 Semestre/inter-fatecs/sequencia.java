import java.util.Scanner;

public class sequencia {
    public static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        String res = "1";
        for (int i = 1; i < n; i++) {
            res = linha(res);
        }
        System.out.println(res);
    }

    public static String linha(String linhaAnterior) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < linhaAnterior.length(); i++) {
            char digito = linhaAnterior.charAt(i);
            int totalDigitos = 1;
            for (; i + 1 < linhaAnterior.length() && linhaAnterior.charAt(i + 1) == digito; i++) {
                totalDigitos++;
            }
            sb.append(String.format("%d%d", totalDigitos, digito - '0'));
        }
        return sb.toString();
    }
}
