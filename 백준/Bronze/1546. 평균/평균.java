import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private int n;
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        double[] arr = new double[n];
        for(int i=0; i<n; i++){
            arr[i] = Double.parseDouble(st.nextToken());
        }
        double max = Arrays.stream(arr).max().getAsDouble();
        System.out.println(Arrays.stream(arr).map((num) -> {
            return num / max * 100;
        }).average().getAsDouble());
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}