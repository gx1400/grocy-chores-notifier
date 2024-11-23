from grocyapi import verify_grocy_api, get_chores_due_next_7_days

def main():
    """Main function to verify the Grocy API and fetch chores."""
    # Verify the Grocy API
    if not verify_grocy_api():
        exit("Verification failed. Exiting script.")

    # Fetch and display chores due in the next 7 days
    get_chores_due_next_7_days()

if __name__ == "__main__":
    main()
