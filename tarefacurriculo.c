#include <stdio.h>


int ehpar(int num) {
    int ehpar;
    if (num%2==0)
    {
        ehpar = 1;
    }
    else 
    {
        ehpar = 0;
    }
    return ehpar;
}

int main(void)
{
  FILE *arq;
  
  char *result;
  int i;
  int periodo, codigo, carga;
  char nome[30];
  int total = 0;

  // Abre um arquivo TEXTO para LEITURA
  arq = fopen("arquivo.txt", "rt");

  if (arq == NULL)  // Se houve erro na abertura
  {
     printf("Problemas na abertura do arquivo\n");
     return 0;
  }
     
     if(arq){
	
      while(fscanf(arq, " %d %d %s %d[^\n]", &periodo, &codigo, nome, &carga) != EOF)
            {
            total = total + carga;
            fgetc(arq);
                    if (ehpar(codigo) == 1){
                        printf("%d GBC%d %s %d\n", periodo , codigo, nome, carga );
                    }
                    else{
                        printf("%d FACOM%d %s %d\n", periodo , codigo, nome, carga );
                    }

            
            }
            fclose(arq);
     }
               printf("%d TOTAL", total);
     return 0;
}