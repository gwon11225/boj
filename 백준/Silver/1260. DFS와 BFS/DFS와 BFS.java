import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[][] nodes = new int[1001][1001];
    static int[] haveNode = new int[1001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            nodes[x][y] = 1;
            nodes[y][x] = 1;
        }

        dfs(v, n);
        System.out.printf("\n");
        haveNode = new int[1001];
        bfs(v, n);
    }

    public static void dfs(int v, int n) {
        haveNode[v] = 1;
        System.out.printf("%d ", v);
        for(int i = 1; i < n + 1; i++) {
            if(haveNode[i] == 1  || nodes[v][i] == 0) continue;
            dfs(i, n);
        }
    }

    public static void bfs(int v, int n) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(v);
        haveNode[v] = 1;

        while (!queue.isEmpty()) {
            int hadNode = queue.poll();
            for(int i = 1; i <= n; i++) {
                if(haveNode[i] == 1 || nodes[hadNode][i] == 0) continue;
                queue.add(i);
                haveNode[i] = 1;
            }
            System.out.print(hadNode+" ");

        }
    }
}