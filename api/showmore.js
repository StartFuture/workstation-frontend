import ShowMore from 'react-show-more';

// ... //

class Foo extends Component {
    render() {
        return (
            <ShowMore
                {* Default options *}
                lines={4}
                more='Show more'
                less='Show less'
                anchorClass=''
            >
                {Solução adotada a fórceps pelas empresas durante os meses de isolamento social, o home office vai se consolidando como algo definitivo em muitos setores, e deverá se tornar uma das principais heranças da pandemia para o futuro do trabalho. Mas um estudo norte-americano mostra que ainda há muito a se desenvolver para que o sistema casa-escritório seja sustentável no longo prazo, ao menos do ponto de vista da saúde e do bem-estar.}
            </ShowMore>
        );
    }
}