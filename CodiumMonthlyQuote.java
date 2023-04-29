// Daily Quote Plugin for JetBrains IDEs

// Author: Ifedayo Akinsira-Olumide

// Email: akinsiraolympicson@gmail.com

import com.intellij.openapi.project.Project;

import com.intellij.openapi.startup.StartupActivity;

import com.intellij.openapi.ui.Messages;

import java.time.LocalDate;

import java.time.Month;

public class DailyQuote implements StartupActivity {

    /**

     * The runActivity method is called when the IDE starts up.

     * It displays a daily quote or joke on the IDE splash screen,

     * depending on the current month.

     *

     * @param project The current project instance.

     */

    @Override

    public void runActivity(Project project) {

        // Get the current date and month.

        LocalDate currentDate = LocalDate.now();

        Month currentMonth = currentDate.getMonth();

        int currentDay = currentDate.getDayOfMonth();

        // Initialize the quote variable.

        String quote = "";

        // Select a quote based on the current month.

        switch (currentMonth) {

            case JANUARY:

                quote = "The journey of a thousand miles begins with one step.";

                break;

            case FEBRUARY:

                quote = "Programming is like sex. One mistake and you have to support it for the rest of your life.";

                break;

            case MARCH:

                quote = "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.";

                break;

            // Add more quotes for other months here...

            default:

                quote = "If at first you don't succeed, call it version 1.0.";

                break;

        }

        // Display the quote on the IDE splash screen.

        Messages.showInfoMessage(quote, "Daily Quote");

    }

}

