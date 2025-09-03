import java.text.Normalizer;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Pattern;

public class cifracesar {
    public static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        while (true) {
            String entrada = scanner.nextLine().replace("\n", "");
            if (entrada.equals("* * *")) {
                break;
            }
            int des = deslocamento(entrada);
            StringBuilder sb = new StringBuilder(entrada);
            for (int i = 0; i < sb.length(); i++) {
                if (Character.isAlphabetic(sb.charAt(i))) {
                    sb.setCharAt(i, (char) deslocar(sb.charAt(i), des));
                }
            }
            list.add(sb.toString());
        }
        for (String s : list) {
            System.out.println(s);
        }
    }

    public static int deslocamento(String s) {
        if (s.charAt(s.length() - 1) == proximoChar(s.charAt(s.length() - 2))) {
            int alvo = Character.toLowerCase(s.charAt(s.length() - 1));
            int des = 0;
            int ch = 'r';
            while (ch != alvo) {
                des++;
                ch = proximoChar(ch);
            }
            return des;
        }
        int alvo = Character.toLowerCase(s.charAt(s.length() - 1));
        int des = 0;
      int ch = 'e';
      while (ch != alvo) {
          des++;
          ch = proximoChar(ch);
      }
      return des;
    }

    public static int proximoChar(int ch) {
        if (ch == 'z') {
            return 'a';
        }
        if (ch == 'Z') {
            return 'A';
        }
        return ch + 1;
    }

    public static int anteriorChar(int ch) {
        if (ch == 'a') {
            return 'z';
        }
        if (ch == 'A') {
            return 'Z';
        }
        return ch - 1;
    }

    public static int deslocar(int ch, int deslocamento) {
        int res = ch;
      for (int i = 0; i < deslocamento; i++) {
          res = anteriorChar(res);
      }
      return res;
    }
}
