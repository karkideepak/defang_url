import java.util.Scanner;

public class DefangURL {
    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Ask for user input
        System.out.print("Enter the URL: ");
        String userUrl = scanner.nextLine();

        // Defang the URL
        String defangedUrl = defangUrl(userUrl);

        // Display the result
        System.out.println("Defanged URL: " + defangedUrl);

        // Close the scanner
        scanner.close();
    }

    // Function to defang the URL
    public static String defangUrl(String url) {
        return url.replace(".", "[.]")
                  .replace("http", "hxxp")
                  .replace(":", "[:]");
    }
}
