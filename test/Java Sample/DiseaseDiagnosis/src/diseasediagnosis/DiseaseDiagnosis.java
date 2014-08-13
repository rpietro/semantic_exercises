package diseasediagnosis;

import com.hp.hpl.jena.graph.Triple;
import com.hp.hpl.jena.query.Query;
import com.hp.hpl.jena.query.QueryExecution;
import com.hp.hpl.jena.query.QueryExecutionFactory;
import com.hp.hpl.jena.query.QueryFactory;
import com.hp.hpl.jena.query.QuerySolution;
import com.hp.hpl.jena.query.ResultSet;
import com.hp.hpl.jena.rdf.model.Model;
import com.hp.hpl.jena.sparql.core.TriplePath;
import com.hp.hpl.jena.sparql.core.Var;
import com.hp.hpl.jena.sparql.syntax.ElementPathBlock;
import com.hp.hpl.jena.sparql.syntax.ElementVisitorBase;
import com.hp.hpl.jena.sparql.syntax.ElementWalker;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.ListIterator;
import java.util.Scanner;
import org.apache.jena.riot.RDFDataMgr;

public class DiseaseDiagnosis {

    public static void main(String[] args) {

        Model model = RDFDataMgr.loadModel("src/jsonld/diseases.jsonld");
        
        List<String> symptoms = Arrays.asList("CryingOften", "Insomnia");

        String Rule = null;
        try {
            Rule = new Scanner(new File("src/inferenceRules/findDiseases.query")).useDelimiter("\\Z").next();
        } catch (FileNotFoundException ex) {
            System.err.println("teste.query not found");
            System.exit(-1);
        }

        Query query = QueryFactory.create(Rule);
        ElementWalker.walk(query.getQueryPattern(),
                new ElementVisitorBase() {
                    @Override
                    public void visit(ElementPathBlock el) {
                        ListIterator<TriplePath> it = el.getPattern().iterator();
                        for (String symptom : symptoms) {
                            it.add( new TriplePath( new Triple(
                                    Var.alloc("disease"), 
                                    model.getProperty("http://diseasesdiagnosis.com/hasSymptom").asNode(), 
                                    model.getResource("http://diseasesdiagnosis.com/" + symptom).asNode() 
                            ) ) );
                        }
                    }
                }
        );

        try (QueryExecution queryExec = QueryExecutionFactory.create(query, model)) {
            ResultSet res = queryExec.execSelect();
            ArrayList<String> diseases = new ArrayList<>();
            while (res.hasNext()) {
                QuerySolution sol = res.nextSolution();
                diseases.add( sol.getLiteral("diseaseName").getString() );
            }
                  
            System.out.println("Given the symptoms: " + symptoms.toString());
            System.out.println("The most likely diseases are: " + diseases.toString());
            
        }
    }
}
