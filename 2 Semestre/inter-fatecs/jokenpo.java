import java.util.Scanner;

public class jokenpo {
    public static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int beatrizPontos = 0;
        int arturPontos = 0;

        while (true) {
            char beatriz = scanner.next().charAt(0);
            char artur = scanner.next().charAt(0);

            if (beatriz == '-' || artur == '-') {
                break;
            }

            int ret = jogada(beatriz, artur);
            if (ret < 0) {
                beatrizPontos++;
            }
            else if (ret > 0) {
                arturPontos++;
            }
        }

        if (beatrizPontos == arturPontos) {
            System.out.println("TIE");
        }
        else if (beatrizPontos > arturPontos) {
            System.out.println("BEATRIZ WIN");
        }
        else {
            System.out.println("ARTUR WIN");
        }
    }

    public static int jogada(char j1, char j2) {
        if (j1 == j2) {
            return 0;
        }

        if (j1 == '*' && j2 == 'O') {
            return 1;
        }
        if (j1 == '*' && j2 == 'V') {
            return -1;
        }

        if (j1 == 'O' && j2 == '*') {
            return -1;
        }
        if (j1 == 'O' && j2 == 'V') {
            return 1;
        }

        if (j1 == 'V' && j2 == '*') {
            return 1;
        }
        if (j1 == 'V' && j2 == 'O') {
            return -1;
        }
        
        return 0;
    }
}
