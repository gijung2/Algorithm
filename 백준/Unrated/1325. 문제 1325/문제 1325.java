import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static ArrayList<Integer>[] graph;
    static int N, M;
    static boolean[] v;
    static int []count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        count = new int[N+1];
        graph = new ArrayList[N+1];
        for(int i =0; i<=N; i++){
            graph[i] = new ArrayList<>();
        }
        for(int i =0; i<M; i++){

            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b= Integer.parseInt(st.nextToken());

            graph[b].add(a);
        }
        int max = Integer.MIN_VALUE;
        for(int i = 1; i<=N; i++){
            v = new boolean[N+1];
            //bfs여러번 출동
            count[i] = bfs(i);
            max = Math.max(max, count[i]);
        }


        //출력
        for(int i =1; i<=N; i++){
            if(count[i] == max){
                System.out.print(i + " ");
            }
        }

    }
    public static int bfs(int start){
        Queue<Integer> q= new ArrayDeque<>();
        v[start] = true;
        q.add(start);
        int cnt = 0;

        while (!q.isEmpty()){

            int cur = q.poll();

            for(int next: graph[cur]){

                if(v[next]) continue;

                cnt++;
                v[next] = true;
                q.add(next);

            }

        }

        return cnt;

    }
}
