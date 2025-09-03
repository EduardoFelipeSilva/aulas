import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class cerco {
  public static Scanner scanner = new Scanner(System.in);
  
  public static void main(String[] args) {
    int casaX = scanner.nextInt();
    int casaY = scanner.nextInt();
    int raio = scanner.nextInt();

    int numeroInimigos = scanner.nextInt();
    List<Inimigo> lista = new ArrayList<>();
    for (int i = 0; i < numeroInimigos; i++) {
      lista.add(new Inimigo(scanner.nextInt(), scanner.nextInt()));
    }

    int inimigosnoraio = 0;

    for (Inimigo i : lista) {
        int x = i.x;
        int y = i.y;

        double raioInimigo = Math.sqrt(x*x+y*y);

        double resposta = Math.PI * raioInimigo* raioInimigo;
    }

    System.out.println(inimigosnoraio);
  }

  public static class Inimigo {
    public int x;
    public int y;

    public Inimigo(int x, int y) {
        this.x = x;
        this.y = y;
    }
  }
}
