import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	//올해 z대학 컴퓨터 공학부에 새로 입학한 민욱이는 학부에 개설된 모든 전공과목을 듣고 졸업하려는 원대한 목표를 세웠다.
	//어떤 과목들은 선수과목이 있어 해당되는 모든 과목을 먼저 이수해야만 해당 과목을 이수할 수 있음.
	//각 과목이 최소한 몇학기부터 들을 수 있는지를 나타내야됨.
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());//과목의수
		int M = Integer.parseInt(st.nextToken());//선수 조건의 수
		
		ArrayList<Integer>[] graph = new ArrayList[N+1];
		int[] indegree = new int[N+1];
		ArrayList<Integer> result = new ArrayList<>();//결과배열로 개수로 사이클 체크도 가능
		int[] project = new int[N+1];
		
		
		//인접리스트 초기화
		for(int i =0; i<=N; i++) {
			graph[i] = new ArrayList<>();
		}
		
		
		for(int i = 0; i< M;  i++) {
			
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			//연결표시
			graph[a].add(b);
			//들어오는 차수 증가
			indegree[b]++;
		}
		
		Queue<Integer> q = new ArrayDeque<>();
		for(int i=1; i<=N; i++) {
			if(indegree[i] == 0) {
				q.add(i);
			}
		}
		int time =1;
		while(!q.isEmpty()) {
			
			int qsize = q.size();
			for(int i =1; i<=qsize; i++) {
				int cur = q.poll();
				
				project[cur] = time;
				result.add(cur);
				for(int next: graph[cur]) {
					
					indegree[next] --;
					
					if(indegree[next] == 0) {
						
						q.add(next);
					}
					
				}
				
			}
			time++;
			
			
		}
		
		
		//출력
		for(int i =1; i<=N; i++) {
			
			System.out.print(project[i] + " ");
		}
		
	}

}
