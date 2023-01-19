import java.io.*;
import java.util.StringTokenizer;

public class Main {
    private int n;
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int recur = Integer.parseInt(st.nextToken());
            String word = st.nextToken();
            for(int j=0; j<word.length(); j++){
                for(int k=0; k<recur; k++){
                    sb.append(word.charAt(j));
                }
            }
            System.out.println(sb.toString());
            sb.setLength(0);
        }
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}