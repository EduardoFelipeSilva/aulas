import java.util.*;

public class lastplayer {
    public static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        int k = scanner.nextInt();

        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            list.add(i);
        }

        int inicio = 0;

        while (list.size() > 1) {
            int res = (inicio + k - 1) % list.size();
            inicio = res;
            list.remove(res);
        }

        System.out.println(list.get(0));
    }
}
