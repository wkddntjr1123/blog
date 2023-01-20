import java.io.*;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Set<Integer> set = new HashSet<>();
        for(int i=0; i<10; i++){
            set.add(Integer.parseInt(br.readLine()) % 42);
        }
        System.out.println(set.size());
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}