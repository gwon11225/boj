import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int [] board = new int[101];
        int [] count = new int[101];
        int rear=-1,front=-1;
        for(int i=1;i<=100;i++){
            board[i]=i;
            count[i]=-1;
        }
        int N,M;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        for (int i=0;i<N+M;i++){
            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            board[S]=E;
        }
        count[1]=0;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        while (queue.size()!=0){
            int temp = queue.poll();
            for(int i=1;i<=6;i++){
                if(temp+i>100){
                    continue;
                }
                int arrive=board[temp+i];
                if(count[arrive]==-1){
                    count[arrive]=count[temp]+1;
                    queue.add(arrive);
                }
            }
        }
        System.out.println(count[100]);
    }
}