import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        char[] line = bufferedReader.readLine().toCharArray();
        int count = 0;

        char[] reverseCharArray = new char[line.length];
        for(int i = 0; i < reverseCharArray.length; i++) {
            reverseCharArray[i] = line[line.length - i - 1];
            if (line[i] == line[0]) {
                count ++;
            }
        }

        if (line.length == count) {
            System.out.println(-1);
        } else if (isEqual(line, reverseCharArray)) {
            System.out.println(line.length - 1);
        } else {
            System.out.println(line.length);
        }
    }

    static boolean isEqual(char[] charArray1, char[] charArray2) {
        for (int i = 0; i < charArray1.length; i++) {
            if(charArray1[i] != charArray2[i]) {
                return false;
            }
        }
        return true;
    }
}