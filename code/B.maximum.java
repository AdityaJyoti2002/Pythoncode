import java.util.Scanner;

public class Main {
    public static int maxWeaponStrength(String L, String R) {
        int maxStrength = 0;
        int minLength = Math.min(L.length(), R.length());
        
        for (int i = 0; i < minLength; i++) {
            int diff = Math.abs(Character.getNumericValue(L.charAt(i)) - Character.getNumericValue(R.charAt(i)));
            maxStrength += diff;
        }
        
        if (L.length() > R.length()) {
            maxStrength += Integer.parseInt(L.substring(minLength));
        } else if (R.length() > L.length()) {
            maxStrength += Integer.parseInt(R.substring(minLength));
        }
        
        return maxStrength;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        // Process each test case
        for (int i = 0; i < t; i++) {
            String L = scanner.next();
            String R = scanner.next();
            int result = maxWeaponStrength(L, R);
            System.out.println(result);
        }
        
        scanner.close();
    }
}
