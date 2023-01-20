import java.io.*;
import java.util.*;
import java.util.stream.Stream;

public class Main {
    int n, m, startV;
    static StringBuilder sb = new StringBuilder();
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] s = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        n = s[0];
        m = s[1];
        startV = s[2];
        List<Integer>[] graph = new ArrayList[n+1];
        for(int i=0; i<=n; i++){
            graph[i] = new ArrayList<>();
        }
        for(int i=0; i<m; i++){
            int[] uv = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            graph[uv[0]].add(uv[1]);
            graph[uv[1]].add(uv[0]);
        }
        for(int i=1; i<=n; i++){
            graph[i].sort(Comparator.naturalOrder());
        }
        dfs(graph, startV, new boolean[n + 1]);
        sb.append("\n");
        bfs(graph, startV, new boolean[n + 1]);
        System.out.println(sb.toString());
    }

    public void dfs(List<Integer>[] graph, int v, boolean[] visited){
        visited[v] = true;
        sb.append(v + " ");
        for(int nv: graph[v]){
            if(!visited[nv]){
                dfs(graph, nv, visited);
            }
        }
    }

    public void bfs(List<Integer>[] graph, int startV, boolean[] visited){
        Deque<Integer> q = new ArrayDeque();
        visited[startV] = true;
        q.add(startV);
        while(q.size() > 0 ){
            int v = q.poll();
            sb.append(v + " ");
            for(int nv: graph[v]){
                if(visited[nv]){
                    continue;
                }
                visited[nv] = true;
                q.add(nv);
            }
        }
    }



    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}