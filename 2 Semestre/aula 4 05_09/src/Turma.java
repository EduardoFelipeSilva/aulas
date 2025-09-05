public class Turma {
    // 1 turma tem N alunos
    // com vetor ou array
    private Aluno alunos[]; //vetor de Alunos 1 para muitos
    private String semestre;
    private int capacidade; // Tamanho maximo
    private int tamanho; //Tamanho atual

    public Turma(int capacidade, String semestre){
        if(capacidade<=0){
            // System.out.println("Capacidade invalida");
            throw new IllegalArgumentException("Capacidade Invalida");
        }else{
            // Definindo capacidade do vetor
            this.alunos = new Aluno[capacidade];
            this.semestre = semestre;
            this.tamanho = 0;
        }

    }

    public boolean inserir(Aluno aluno){
        if(tamanho == alunos.length){
            return false; // que o vetor esta cheio
        }else {
            alunos[tamanho++] = aluno;
            return true; // Aluno inserido no vetor
        }
    }

    public Aluno[] listar(){
        Aluno[] copia = new Aluno[tamanho];
        for (int i = 0; i< tamanho; i++){
            copia[i] = alunos[i];
        }
        return copia;
    }

    public boolean remover(int ra){
        for (int i = 0; i < tamanho; i++){
            if(alunos[i].getRa()==ra){
                alunos[i] = alunos[tamanho-1];
                alunos[tamanho-1] = null;
                tamanho--;
                return true;
            }
        }
        return false;

    }

    public Aluno localizarRa(int ra){
        for(int i= 0; i<tamanho;i++){
            if(alunos[i].getRa() == ra){
                return alunos[i];
            }
        }
        return null;
    }

    public int capacidadeTurma(){
        return alunos.length - tamanho;
    }
    

    

}
