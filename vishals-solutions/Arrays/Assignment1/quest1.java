public class quest1 {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        
        // Method 1: Using for loop
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        
        // Method 2: Using enhanced for loop
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
        
        // Method 3: Using Arrays.toString()
        System.out.println(java.util.Arrays.toString(arr));
    }
}