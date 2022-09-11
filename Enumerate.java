import java.util.ArrayList;
import java.util.List;

public class Enumerate {
    public static void main(String[] args) {
        List<String> arr = new ArrayList<String>();

        arr.add("Mari");
        arr.add("Joy");
        arr.add("Butsi");

        for (int i = 0; i < arr.size(); i++) {
            System.out.println(arr.get(i) + " " + i);
        }

        for (String s : arr) {
            System.out.println(s);
        }

    }
}