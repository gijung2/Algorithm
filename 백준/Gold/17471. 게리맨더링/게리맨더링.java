import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    //백준시는 N개의 구역으로 나누어짐 1~N
    //각 구역은 두 선거구 중 하나에 포함되어야 한다.
    //선거구는 최소한 한개는 있어야 되고, 두개로 나눠진 선거구는 연결되어 있어야됨.
    //부분집한으로 선거구를 뽑고, 선거구 연결체크를 bfs로 한다.
    //나눠진선거구는 arraylist방식으로 하자

    static int N;
    static ArrayList<Integer>[] graph;
    static int[] human;
    static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        human = new int[N+1];//사람인원수
        graph = new ArrayList[N+1];

        for(int i=0; i<=N; i++){
            graph[i] = new ArrayList<>();
        }
        answer = Integer.MAX_VALUE;
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=1; i<=N;i++){
            human[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 1; i<=N; i++){
            st = new StringTokenizer(br.readLine());

            int k = Integer.parseInt(st.nextToken());

            for(int j = 0; j<k; j++){
                int temp = Integer.parseInt(st.nextToken());
                graph[i].add(temp);
                graph[temp].add(i);
                //무방향 그래프
            }
        }


        //부분집합으로 구역 나누기
        dfs(1, 0, 0, new ArrayList<>(), new ArrayList<>());


        //출력
        if(answer == Integer.MAX_VALUE){
            System.out.println(-1);
        } else{
            System.out.println(answer);
        }
    }

    //N개의 구역을 다 나누면 끝, 뽑은 개수도 다룰거임, 리스트로 후보 배열도 다룰것
    public static void dfs(int depth, int acnt, int bcnt, ArrayList<Integer> alist, ArrayList<Integer> blist){

        if(depth ==N+1) {

            //먼저 최소한 한개에 있는지, 할필요가없음
            if (acnt == 0 || bcnt == 0) {
                return;
            }

            //구역 연결 체크
            int temp1 = bfs(alist);
            int temp2 = bfs(blist);
            //bfs를 두 번 보낼거임

            if(temp1 != -1 && temp2!=-1){
                int diff = Math.abs(temp1 -temp2);
                answer = Math.min(diff, answer);
                return;
            }

            return;
        }
        alist.add(depth);
        dfs(depth+1, acnt+1, bcnt, alist, blist);
        alist.remove(alist.size()-1);

        blist.add(depth);
        dfs(depth+1, acnt, bcnt+1, alist, blist);
        blist.remove(blist.size()-1);
    }

    public static int bfs(ArrayList<Integer>list){
        boolean [] select = new boolean[N+1];
        boolean [] v = new boolean[N+1];
        int start = 0;
        int scnt=0;
        for(int temp: list){
            start = temp;
            select[temp] = true;// 해당하는
            scnt++;
        }

        Queue<Integer> q = new ArrayDeque<>();
        v[start] = true;
        q.add(start);
        int vcnt =1;
        int sum = human[start];
        while(!q.isEmpty()){
            int cur = q.poll();

            for(int next: graph[cur]){
                if(v[next]) continue; //방문한적이 있으면 갈 필요없음
                if(select[next] == false) continue;//내영역이 아님

                vcnt++;
                sum += human[next];
                v[next] = true;
                q.add(next);

            }

        }

        //둘이 같은지 체크해야됨.
        if(vcnt == scnt){

            return sum;
        }



        return -1; //-1을 넘기면 둘이 같은게 아님.
    }

}
