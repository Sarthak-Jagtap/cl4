import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;

public class GradeReducer extends MapReduceBase
implements Reducer<Text, IntWritable,
                   Text, Text> {

    public void reduce(Text key,
                       Iterator<IntWritable> values,
                       OutputCollector<Text, Text> output,
                       Reporter reporter) throws IOException {

        int total = 0;
        int count = 0;

        while(values.hasNext()) {

            total += values.next().get();

            count++;
        }

        int average = total / count;

        String grade;

        if(average >= 90) {
            grade = "A";
        }
        else if(average >= 80) {
            grade = "B";
        }
        else if(average >= 70) {
            grade = "C";
        }
        else if(average >= 60) {
            grade = "D";
        }
        else {
            grade = "F";
        }

        output.collect(
        key,
        new Text("Average = "
        + average +
        " Grade = " + grade));
    }
}
