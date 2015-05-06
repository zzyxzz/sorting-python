int get_second_biggest(int* array,int n)
{
    mergeorder(array,n); // tournament: n-1 comparisons
    int second_best = array[n/2];
    for(int i = n/4; i > 0; i /= 2) 
    {
        if(array[i] > second_best) // log(n) - 1 comparisons
            second_best = array[i];
    }
    return second_best;
}
void mergeorder(int* array, int n)
{
    if (n < 2)
        return;
    mergeorder(array, n/2);
    mergeorder(array + n/2, n/2);
    merge(array, n);
}

void merge(int* array, int n)
{
    if (*array < *(array + n/2))
    {
        for (int i = 0;i < n/2;i++)
            swap(&array[i],&array[i + n/2]);
    }
}
void swap(int* a, int* b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
