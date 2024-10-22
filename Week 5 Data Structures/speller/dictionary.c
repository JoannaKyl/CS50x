// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // find out which bucket the word belongs to, e.g. A should be in table[0]. Z should be in
    // table[25]
    int index = hash(word);
    
    // traverse the linked list of that bucket
    node *cursor = table[index];
    while (cursor != NULL)
    {
        // End the traversal if the word is equal
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        // otherwise, look at the next word
        else
        {
            cursor = cursor->next;
        }
    }
    // return false if the word cannot be found after finishing the traversal
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Look at the beginning character of the word, and figure out the right bucket, e.g. A goes to
    // 0, Z goes to 25
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        return false;
    }

    // Read each word in the file
    // Add each word to the hash table
    char new_word[LENGTH + 1];
    while (fscanf(source, "%s", new_word) != EOF)
    {
        // Create a new node to store the new word
        node *new_node = malloc(sizeof(node));
        strcpy(new_node->word, new_word);
        new_node->next = NULL;

        // Find out which A-Z bucket the new word is in
        int index = hash(new_word);
        node *head_node = table[index];
        // If the bucket is empty now, the head of the bucket is the new node
        if (head_node == NULL)
        {
            table[index] = new_node;
        }
        // Otherwise, prepend the new word to the linked list
        else
        {
            new_node->next = head_node->next;
            head_node->next = new_node;
        }
    }

    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    int count = 0;
    // traverse the 26 buckets
    for (int i = 0; i < N; i++)
    {
        // traverese the linked list inside each bucket
        node *cursor = table[i];
        while (cursor != NULL)
        {
            count++;
            cursor = cursor->next;
        }
    }
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // traverse the 26 buckets
    for (int i = 0; i < N; i++)
    {
        // traverese the linked list inside each bucket
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}
