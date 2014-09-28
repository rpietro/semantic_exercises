package diseasediagnosis;

import com.hp.hpl.jena.query.Query;
import com.hp.hpl.jena.query.QueryExecution;
import com.hp.hpl.jena.query.QueryExecutionFactory;
import com.hp.hpl.jena.query.QueryFactory;
import com.hp.hpl.jena.query.QuerySolution;
import com.hp.hpl.jena.query.ResultSet;
import com.hp.hpl.jena.rdf.model.Model;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import org.apache.jena.riot.RDFDataMgr;

public class DiseaseDiagnosis {

    public static void main(String[] args) {

        Model model = RDFDataMgr.loadModel("src/jsonld/MajorDepressiveDisorderUseCase.jsonld");

        String Rule = null;
        try {
            Rule = new Scanner(new File("src/inferenceRules/findDiseases.query")).useDelimiter("\\Z").next();
        } catch (FileNotFoundException ex) {
            System.err.println("findDiseases.query not found");
            System.exit(-1);
        }

        Query query = QueryFactory.create(Rule);

        try (QueryExecution queryExec = QueryExecutionFactory.create(query, model)) {
            ResultSet res = queryExec.execSelect();
            ArrayList<String> diseases = new ArrayList<>();
            while (res.hasNext()) {
                QuerySolution sol = res.nextSolution();
                diseases.add(sol.getLiteral("?diseaseName").getString());

            }

            System.out.println("The most likely diseases are: " + diseases.toString());

        }
    }
}
