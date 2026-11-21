import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

class edge implements Comparable<edge>{
    int from, to, weight;

    edge(int from, int to, int weight){
        this.from =from;
        this.to = to;
        this.weight =weight;
    }

    @Override
    public int compareTo(edge o) {
        return Integer.compare(this.weight, o.weight);
    }
}

public class Main {

    static int[]parent;
    //find
    public static int find (int x){

        if(parent[x] == x){
            return x;
        }

        return parent[x] = find(parent[x]);
    }
    //union
    public static boolean union(int a, int b){

        int X = find(a);
        int Y = find(b);

        if(X == Y){
            return false;
        }

        //union한거임
        parent[X] = Y;
        return true;
    }

    static int V, E;
    static edge[] edgelist;
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        edgelist = new edge[E];
        parent= new int[V+1];

        for(int i = 1; i<= V; i++){
            parent[i] = i;
        }
        for(int i =0; i<E; i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to  =Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            edgelist[i] = new edge(from, to, weight);

        }

        Arrays.sort(edgelist);

        int answer = 0;
        int count = 0;

        for(int i =0; i<E; i++){
            edge cur = edgelist[i];

            if(union(cur.from, cur.to)){
                answer += cur.weight;
                count++;

                if(count == V-1){
                    break;
                }
            }
        }

        System.out.println(answer);

    }



}
