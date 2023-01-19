import java.io.*;

public class Main {
    private int n;
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        recur(n);
    }
    public void recur(int n){
        if(n<1){
            return;
        }
        System.out.println(n);
        recur(n-1);
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}