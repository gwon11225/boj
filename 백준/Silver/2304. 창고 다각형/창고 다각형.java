import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int [] highArray = new int[1001];
        int index,high,answer=0;
        int max=0,maxIndex=2000;
        int N = Integer.parseInt(br.readLine());

        for(int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            index = Integer.parseInt(st.nextToken());
            high = Integer.parseInt(st.nextToken());
            highArray[index]=high;
            if(max<high){
                max=high;
                maxIndex=index;
            }
        }
        answer+=max;
        max=0;
        for(int i=1;i<maxIndex;i++){
            if(highArray[i]>max){
                max=highArray[i];
            }
            answer+=max;
        }

        max=0;
        for(int i=1000;i>maxIndex;i--){
            if(highArray[i]>max){
                max=highArray[i];
            }
            answer+=max;
        }
        System.out.println(answer);
    }
}