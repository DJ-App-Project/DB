package main

import (
	"context"
	"encoding/csv"
	"log"
	"os"

	"github.com/google/go-github/github"
	"golang.org/x/oauth2"
)

func main() {
	// Open the CSV file
	file, err := os.Open("github_issues.csv")
	if err != nil {
		log.Fatalf("Failed to open CSV file: %s", err)
	}
	defer file.Close()

	// Read CSV content
	reader := csv.NewReader(file)
	records, err := reader.ReadAll()
	if err != nil {
		log.Fatalf("Failed to read CSV file: %s", err)
	}

	// Authenticate with GitHub
	ctx := context.Background()
	ts := oauth2.StaticTokenSource(
		&oauth2.Token{AccessToken: "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"},
	)
	tc := oauth2.NewClient(ctx, ts)
	client := github.NewClient(tc)

	// Iterate over CSV records and create issues
	for _, record := range records[1:] { // Skip header
		title, body, _, status, _ := record[0], record[1], record[2], record[3], record[4]

		issueRequest := &github.IssueRequest{
			Title: github.String(title),
			Body:  github.String(body),
			State: github.String(status),
		}

		issue, _, err := client.Issues.Create(ctx, "DJ-App-Project", "DB", issueRequest)
		if err != nil {
			log.Printf("Error creating issue: %s", err)
			continue
		}

		log.Printf("Issue created: %s", issue.GetHTMLURL())
	}
}
