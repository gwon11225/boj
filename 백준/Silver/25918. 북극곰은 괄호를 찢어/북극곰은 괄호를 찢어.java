import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int length = Integer.parseInt(br.readLine());
        String st = br.readLine();
        int day = 0;

        Stack<Character> stack = new Stack<>();

        for (int i=0;i<length;i++){
            if(stack.isEmpty() || Objects.equals(stack.peek(),st.charAt(i))) stack.push(st.charAt(i));
            else stack.pop();

            day = Math.max(day,stack.size());
        }
        if(stack.isEmpty()) System.out.println(day);
        else System.out.println("-1");
    }
}