```mermaid
classDiagram

    class Colaborador {
        +String nome
        +String cargo
        +String setor
        +List<Avaliacao> avaliacoesRecebidas
        +List<Avaliacao> avaliacoesRealizadas
    }

    class Gerente {
        +List<Colaborador> equipeGerenciada
    }
    Gerente --|> Colaborador

    class TimeRH {
        +List<RelatorioDesempenho> analises
        +decidirPromocao()
        +sugerirTreinamento()
    }
    TimeRH --|> Colaborador

    class Avaliacao {
        +Colaborador colaboradorAvaliado
        +Colaborador avaliador
        +Date data
        +List<Criterio> criterios
        +int nota
        +String feedback
    }
    Colaborador --> Avaliacao : realiza
    Avaliacao --> Criterio : usa

    class Criterio {
        +String nome
        +String descricao
        +int peso
    }

    class Departamento {
        +String nome
        +Gerente gestorResponsavel
        +List<Colaborador> equipe
    }
    Departamento --> Gerente : gerenciadoPor
    Departamento --> Colaborador : possui

    class RelatorioDesempenho {
        +Colaborador colaborador
        +String periodo
        +int notaFinal
        +String recomendacoes
    }
    RelatorioDesempenho --> Colaborador

    class ConsultorExterno {
        +String nome
        +String especialidade
        +analisarDados()
        +sugerirMelhorias()
    }
    ConsultorExterno --> Avaliacao : analisa

    class EquipeTI {
        +homologarSistema()
        +manterSistema()
    }

    class Executivo {
        +String cargo
        +visualizarRelatorios()
    }
    Executivo --> RelatorioDesempenho : acessa

