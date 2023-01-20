import java.io.*;

public class Main {
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int hour = Integer.parseInt(s[0]), minute = Integer.parseInt(s[1]);
        minute -= 45;
        if (minute < 0){
            hour -= 1;
            minute += 60;
            if (hour < 0){
                hour = 23;
            }
        }
        System.out.println(hour + " " + minute);
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}